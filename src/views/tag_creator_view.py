from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsabilidade para interagir com HTTP
    '''

    def validate_and_create(self, http_request: HttpRequest):

        body = http_request.body
        product_code = body['product_code']

        # regras de negocio
        print("Estou na minha View")
        
        # retorno http
        return HttpResponse(status_code=200, body={"Hello": "World"})
