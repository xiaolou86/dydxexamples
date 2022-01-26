from dydx3 import Client
from dydx3 import constants
from dydx3 import epoch_seconds_to_iso
import os
import time

########################## YOU FILL THIS OUT #################
_private_key='<FILL_THIS_OUT>'
_api_key='<FILL_THIS_OUT>'
_api_secret='<FILL_THIS_OUT>'
_api_passphrase='<FILL_THIS_OUT>'
_stark_private_key='<FILL_THIS_OUT>'
_eth_address='<FILL_THIS_OUT>'
_network_id=str(constants.NETWORK_ID_ROPSTEN)
#_network_id is set to either str(constants.NETWORK_ID_MAINNET) or str(constants.NETWORK_ID_ROPSTEN)
_api_host=constants.API_HOST_ROPSTEN
#_api_host is set to either constants.API_HOST_MAINNET or constants.API_HOST_ROPSTEN
##############################################################

client = Client(
        host = _api_host,
        default_ethereum_address=_eth_address,
        eth_private_key=_private_key,
        network_id = _network_id
)
stark_private_key = client.onboarding.derive_stark_key()
client.stark_private_key = stark_private_key
get_account_result = client.private.get_account(
        ethereum_address=_eth_address
)
account = get_account_result.data['account']
one_minute_from_now_iso = epoch_seconds_to_iso(time.time() + 70)
create_order_result = client.private.create_order(
        position_id=account['positionId'],
        market=constants.MARKET_BTC_USD,
        side=constants.ORDER_SIDE_BUY,
        order_type=constants.ORDER_TYPE_LIMIT,
        post_only=False,
        size='0.001',
        price='1000',
        limit_fee='0.1',
        expiration=one_minute_from_now_iso,
)
