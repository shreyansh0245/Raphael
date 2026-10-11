"""
Smoke tests for Phase 0 setup verification.

Test 1: package_version — confirms the raphael package is importable and
        exposes the expected __version__ string.

Test 2: dependency_imports — parametrized over all eight Phase 0 dependencies;
        each must import without error. No datasets, network access,
        credentials, or computation required.
"""

import importlib

import pytest

import raphael


def test_package_version() -> None:
    """The raphael package is importable and has the expected version."""
    assert hasattr(raphael, "__version__"), "raphael.__version__ is missing"
    assert raphael.__version__ == "0.1.0", (
        f"Expected '0.1.0', got '{raphael.__version__}'"
    )


PHASE_0_DEPENDENCIES = [
    "numpy",
    "pandas",
    "sklearn",       # import name for scikit-learn
    "matplotlib",
    "seaborn",
    "jupyter",
    "pytest",
    "dotenv",        # import name for python-dotenv
]


@pytest.mark.parametrize("module_name", PHASE_0_DEPENDENCIES)
def test_dependency_imports(module_name: str) -> None:
    """Every approved Phase 0 dependency can be imported."""
    importlib.import_module(module_name)
