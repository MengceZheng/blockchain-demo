import requests
import base64
import ecdsa
import click

@click.command()
@click.option('-g', 'generate_keys', is_flag=True, help='Generate ECDSA key pair')
@click.option('-s', 'send_message', is_flag=True, help='Send message using signature')
@click.option('-m', help='Message to transmit')
@click.option('-f', help='From address')
@click.option('-t', help='To address')
@click.option('-k', help='Private key')
@click.option('-o', 'memo', help='Memo for message')
def client(generate_keys, send_message, m, f, t, k, memo):
    if generate_keys:
        public_key, private_key = generate_ECDSA_keys()
        click.echo("")
        click.echo("Address    : {0}".format(public_key))
        click.echo("Private key: {0}".format(private_key))
        click.echo("")
    elif send_message:
        if m and f and t and k:
            response = send_transaction(f, t, m, k, memo)
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

def send_transaction(from_address, to_address, message, private_key, memo):
    if len(private_key) == 64:
        signature, message = sign_ECDSA_msg(private_key, message)
        url = "http://localhost:8080/post"
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