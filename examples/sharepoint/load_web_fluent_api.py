from office365.runtime.auth.clientCredential import ClientCredential
from office365.sharepoint.client_context import ClientContext
from settings import settings

credentials = ClientCredential(settings['client_credentials']['client_id'],
                               settings['client_credentials']['client_secret'])
ctx = ClientContext(settings['url']).with_credentials(credentials)

target_web = ctx.web.load().execute_query()
print(target_web.url)
