import requests
import base64
import ecdsa
import click

@click.command()
@click.option('-g', 'generate_keys', is_flag=True, help='Generate ECDSA key pair')
@click.option('-s', 'send_message', is_flag=True, help='Send message using signature')
@click.option('--host', default='localhost', help='Server host')
@click.option('--port', default=8080, help='Server port')
@click.option('--message', '-m', help='Message to transmit')
@click.option('--from-address', '-fa', help='From address')
@click.option('--to-address', '-ta', help='To address')
@click.option('--private-key', '-k', help='Private key')
@click.option('--memo', '-o', help='Memo for message')
def client(generate_keys, send_message, host, port, message, from_address, to_address, private_key, memo):
    if generate_keys:
        public_key, private_key = generate_ECDSA_keys()
        click.echo("")
        click.echo("User Host  : {0}".format(host))
        click.echo("User Port  : {0}".format(port))
        click.echo("Address    : {0}".format(public_key))
        click.echo("Private key: {0}".format(private_key))
        click.echo("")
    elif send_message:
        if all([host, port, message, from_address, to_address, private_key, memo]):
            response = send_transaction(host, port, message, from_address, to_address, private_key, memo)
            click.echo("")
            click.echo(response)
        else:
            click.echo("Missing required arguments.")

def generate_ECDSA_keys():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    private_key = sk.to_string().hex()
    vk = sk.get_verifying_key()
    public_key = vk.to_string().hex()
    public_key = base64.b64encode(bytes.fromhex(public_key))
    return public_key.decode(), private_key

def sign_ECDSA_msg(private_key, message):
    bmessage = message.encode()
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    signature = base64.b64encode(sk.sign(bmessage))
    return signature, message

def send_transaction(host, port, message, from_address, to_address, private_key, memo):
    if len(private_key) == 64:
        signature, message = sign_ECDSA_msg(private_key, message)
        url = f"http://{host}:{port}/post"
        data = {
            "from_address": from_address,
            "to_address": to_address,
            "message": message,
            "signature": signature,
            "memo": memo
        }
        response = requests.post(url, data=data)
        return response.text
    else:
        return "Please verify and try again."

if __name__ == '__main__':
    client()