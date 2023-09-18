"""Fixtures for all integration tests"""
import os
import subprocess
import pytest



@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown_server():
    """ Sets up a server for tests and shut it down when it is finished"""
    # Run server
    server_file = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                "../..", "edgepi_rpc_server.py"))

    with subprocess.Popen(
        ['python', server_file, '-c','./edgepi_rpc_server.conf']
    ) as server_process:
        # Run testpy tests
        yield
        # Terminate server
        server_process.terminate()
        server_process.wait()
