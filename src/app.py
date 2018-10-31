from metaendpoints.apiserver import serve

from src.routes_v1 import reg_server_v1
from src.routes_v2 import reg_server_v2

if __name__ == '__main__':
    serve([
        reg_server_v1,
        reg_server_v2
    ])
