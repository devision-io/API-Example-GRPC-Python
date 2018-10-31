from metaendpoints.apimethod import Api

from src.service.cbr_service import get_rates
from src.v1 import example_pb2
from src.v1 import example_pb2_grpc


class CurrencyRateServicer(example_pb2_grpc.CurrencyRateServicer):

    @Api(
        scopes=["meta.dev"]
    )
    def ListCbrRates(self, request: example_pb2.ListCbrRatesRequest, context):
        date = request.date

        rates = []
        for rate in get_rates(date):
            rates.append(example_pb2.CbrRate(
                date=date,
                char_code=rate['char_code'],
                rate=rate['rate']
            ))
        return example_pb2.ListCbrRatesResponse(rates=rates)


class UserServicer(example_pb2_grpc.UserServicer):

    def GetMe(self, request, context):
        return example_pb2.GetMeResponse(
            user_id=context.user_id
        )


# Регистрируем роуты в GRPC сервере
def reg_server_v1(server):
    example_pb2_grpc.add_CurrencyRateServicer_to_server(CurrencyRateServicer(), server)
    example_pb2_grpc.add_UserServicer_to_server(UserServicer(), server)
