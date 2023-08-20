import httpx
from httpx_socks import AsyncProxyTransport

class GetProxy:

    async def validation_proxy(self, proxy, header):
        transport = AsyncProxyTransport.from_url(proxy)
        async with httpx.AsyncClient(transport=transport, headers=header, timeout=10) as client:
            response = await client.get('http://ipwhois.app/json/')
            return {
                'status': response.json()['success'],
                'country': response.json()['country'],
                }

    def get_proxy(self, http=None, socks4=None, socks5=None, unknown=None):
        """Path to proxy file(s)"""
        proxy_list = []
        # Use the provided proxy
        proxy_list.append("http://giorgos123-zone-resi:giorgos321@pr.pyproxy.com:16666")
        return proxy_list
