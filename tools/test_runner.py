#!/usr/bin/env python3
"""
Test Runner Tool
Automatically discovers and runs all test cases in the repository
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple

class TestRunner:
    def __init__(self, root_dir: str = None):
        """Initialize test runner with repository root directory"""
        self.root_dir = root_dir or Path(__file__).parent.parent
        self.results = []
    
    def find_test_files(self) -> List[Path]:
        """Find all test_cases.py files in the repository"""
        test_files = []
        problems_dir = Path(self.root_dir) / "problems"
        
        if not problems_dir.exists():
            print(f"❌ Problems directory not found: {problems_dir}")
            return test_files
        
        for test_file in problems_dir.rglob("test_cases.py"):
            test_files.append(test_file)
        
        return sorted(test_files)
    
    def run_test_file(self, test_file: Path) -> Tuple[bool, str, str]:
        """
        Run a single test file using pytest
        
        Returns:
            (success, output, error)
        """
        try:
            # Change to the directory containing the test file
            test_dir = test_file.parent
            
            # Run pytest on the test file
            result = subprocess.run(
                ["python", "-m", "pytest", str(test_file), "-v", "--tb=short"],
                cwd=test_dir,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            success = result.returncode == 0
            return success, result.stdout, result.stderr
            
        except subprocess.TimeoutExpired:
            return False, "", "Test timed out after 30 seconds"
        except Exception as e:
            return False, "", str(e)
    
    def get_problem_name(self, test_file: Path) -> str:
        """Extract problem name from file path"""
        # Get the parent directory name (e.g., LC78-subsets)
        return test_file.parent.name
    
    def run_all_tests(self, verbose: bool = True) -> dict:
        """
        Run all test files and return summary
        
        Returns:
            Dictionary with test results
        """
        test_files = self.find_test_files()
        
        if not test_files:
            print("❌ No test files found")
            return {"total": 0, "passed": 0, "failed": 0, "errors": []}
        
        print(f"🔍 Found {len(test_files)} test files\n")
        print("=" * 70)
        
        passed = 0
        failed = 0
        errors = []
        
        for i, test_file in enumerate(test_files, 1):
            problem_name = self.get_problem_name(test_file)
            relative_path = test_file.relative_to(self.root_dir)
            
            print(f"\n[{i}/{len(test_files)}] Testing: {problem_name}")
            print(f"    File: {relative_path}")
            
            success, output, error = self.run_test_file(test_file)
            
            if success:
                print(f"    ✅ PASSED")
                passed += 1
            else:
                print(f"    ❌ FAILED")
                failed += 1
                errors.append({
                    "problem": problem_name,
                    "file": str(relative_path),
                    "output": output,
                    "error": error
                })
            
            if verbose and (output or error):
                print(f"\n    Output:")
                if output:
                    for line in output.split('\n')[:10]:  # Show first 10 lines
                        print(f"    {line}")
                if error:
                    print(f"    Error: {error}")
        
        print("\n" + "=" * 70)
        print(f"\n📊 Test Summary:")
        print(f"   Total: {len(test_files)}")
        print(f"   ✅ Passed: {passed}")
        print(f"   ❌ Failed: {failed}")
        print(f"   Success Rate: {passed/len(test_files)*100:.1f}%")
        
        if errors:
            print(f"\n❌ Failed Tests:")
            for error in errors:
                print(f"   - {error['problem']}")
        
        return {
            "total": len(test_files),
            "passed": passed,
            "failed": failed,
            "errors": errors
        }
    
    def run_specific_problem(self, problem_name: str) -> bool:
        """Run tests for a specific problem"""
        test_files = self.find_test_files()
        
        for test_file in test_files:
            if problem_name.lower() in test_file.parent.name.lower():
                print(f"🔍 Running tests for: {test_file.parent.name}")
                success, output, error = self.run_test_file(test_file)
                
                print(output)
                if error:
                    print(f"Error: {error}", file=sys.stderr)
                
                return success
        
        print(f"❌ Problem '{problem_name}' not found")
        return False


def main():
    """Main entry point for test runner"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Run tests for DSA problems",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all tests
  python test_runner.py
  
  # Run tests for a specific problem
  python test_runner.py --problem LC78
  python test_runner.py -p subsets
  
  # Run all tests with minimal output
  python test_runner.py --quiet
        """
    )
    
    parser.add_argument(
        "-p", "--problem",
        type=str,
        help="Run tests for a specific problem (e.g., LC78 or subsets)"
    )
    
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Minimize output (don't show detailed test results)"
    )
    
    parser.add_argument(
        "--root",
        type=str,
        help="Repository root directory (default: parent of this script)"
    )
    
    args = parser.parse_args()
    
    # Create test runner
    runner = TestRunner(root_dir=args.root)
    
    # Run tests
    if args.problem:
        success = runner.run_specific_problem(args.problem)
        sys.exit(0 if success else 1)
    else:
        results = runner.run_all_tests(verbose=not args.quiet)
        sys.exit(0 if results["failed"] == 0 else 1)


if __name__ == "__main__":
    main()
