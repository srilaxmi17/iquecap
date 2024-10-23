# # parsers.py

# from rest_framework.parsers import MultiPartParser, JSONParser
# from rest_framework.exceptions import ParseError
# from django.http.multipartparser import MultiPartParser as DjangoMultiPartParser

# class MultiPartJsonParser(MultiPartParser):
#     """
#     Custom parser to handle multipart/form-data with JSON content.
#     """

#     def parse(self, stream, media_type=None, parser_context=None):
#         parser_context = parser_context or {}
#         request = parser_context['request']
#         encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

#         meta_data = JSONParser().parse(stream, media_type, parser_context)
        
#         if not isinstance(meta_data, dict):
#             raise ParseError("JSON data must be a dictionary")

#         stream.seek(0)  # Reset stream position for MultiPartParser
#         upload_data = DjangoMultiPartParser(request.META, request, stream, request.upload_handlers, encoding).parse()

#         # Combine parsed data
#         data = {
#             **meta_data,
#             **upload_data[0]
#         }
#         files = upload_data[1]

#         return data, files
