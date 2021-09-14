
asset_price = {'error':False}

def symbol_ticker_callback(msg):
    """
    Function to process the incoming WebSocket messages
    param msg: input message
    """
    if msg['e'] != 'error':
        print('current close price:',msg['c'])
        asset_price['last'] = msg['c']
        asset_price['bid'] = msg['b']
        asset_price['last'] = msg['a']
        asset_price['error'] = False
    else:
        asset_price['error'] = True
        
def streaming_symbol_ticker(msg):
    """
    Function to process the received messages
    param msg: input message
    """
    print(f"message type: {msg['e']}")
    print(f"close price: {msg['c']}")
    print(f"best ask price: {msg['a']}")
    print(f"best bid price: {msg['b']}")
    print("---------------------------")
    
def kline_callback(msg):
    #print(f"message type: {msg['e']}")
    print(f"kline data:")
    print(msg)
    print("---------------------------")
