"""Integration test setup for RPC Server"""
import subprocess
import pytest

@pytest.fixture(scope="session", autouse=True)
def setup_server():
    """Server Setup"""
    subprocess.run(["bash", "./start_server.sh"], check=True)
