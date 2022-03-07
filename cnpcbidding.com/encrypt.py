import base64
import traceback

from Crypto.Cipher import AES, PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad

BLOCK_SIZE = 16

from tools import *

privateKey = "MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAITfvlC8+Nr+vz3DnhuCWW41ax8PG+rCiXt/f4XjRMlj9ZC2AuMMbtHLsTMLhCrhgHt1MxdcoYtqvQfxu4AVOh6pZrxMr2AiyNpw8SecmM3m0YWYNc7tnUB6/vlLyQduikD4qaxNiB5FcUiRpiRoLpz7rT6UV+/zDh+ibgvZRLDRAgMBAAECgYB7/mMV6tJ7YkBKPdK8Lw6PZq/5Att1XmZ3ZYo2Adg96tbMXN0izYZYprFMRhHnBhokm0C7K0jg1hFiaXUkWCqr83H+Y+DZ7js9NDhApPYAELQDIu288/nz34mjU/wnIGWP6WK5PCd1QjR8ltFay1TDLecdavHHjWGfHOMYnY5/dQJBAOZ4ICB+VrXMwR8KUR3r420YAHPwQDQKDetMHwgYHtFUH/k3CtKzPrltx103OhQcKyfrkoPj8SREZZISaBEQL6cCQQCTl+pjOSMud4hFTvfTnkGx9EZT3dBAv31ZfzHCu4g41FxRLyJLY6iKce069IhMjC2gfoLtwDLM/dKzRAuw9+rHAkAd9/zlfMg1t7xdFvBZXbUjGH3mlZUjrzMEJ8/ZM5m+SpwlwfyMTXaYkifcfTP2LXuHI2DX+an/t00l43LY1Sv9AkAEgQ5WGNhKArvV4aMOgjXfCGVdCdfhIfbhVFBgcPinQ1PN5nJVeqUaFH/43J2MOHrr+vBj8Qmb1+MmNV1l+SrhAkArJjCosjMI32RT3GmC6+gwxADR9Ib53yDHwRoMeO34dgK3hj3+e66Jhpcht3AjXBVs7bF9xzXcePpxxCka9cEv";

private_key = f'-----BEGIN ENCRYPTED PRIVATE KEY-----\n{privateKey}\n-----END ENCRYPTED PRIVATE KEY-----'

publicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCfXfMzgg4m5RRLg2vcrYBFN4sBhE1VtW1sBkXxC5wtCRaOZv0kudk9CIQfU6c+eEaaZKUnygxHWdSqdwURCE0IKgLcolXF+RHmu/rl977FfjRg9pAkBg5z05PfHDqWqkIsqX0iRaSP31BUZOgtwafbiBv2dBvRBMdq03ty4q8OQQIDAQAB";
public_key = f'-----BEGIN PUBLIC KEY-----\n{publicKey}\n-----END PUBLIC KEY-----'


def randomString(length=32):
    chars_ = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'  # 默认去掉了容易混淆的字符oOLl, 9gq, Vv, Uu, I1
    max_pos = len(chars_)
    pwd = ''
    import random
    for i in range(length):
        pwd += chars_[random.randint(0, max_pos - 1)]
    return pwd


def main():
    key = "电子科技大学"
    userData = {'pageSize': 15,
                'title': key,
                'pageNo': 1,
                'pid': 198,
                'categoryId': 199,
                'projectType': ''
                }
    data = encrypt_data(userData)
    print(data)

def encrypt_data(data):
    random_str = randomString(16)
    key = random_str.encode()
    srcs = json.dumps(data).encode()
    AE = AES.new(key, AES.MODE_ECB)
    result = AE.encrypt(pad(srcs, block_size=BLOCK_SIZE))
    request_data = base64.b64encode(result).decode()

    cipher = PKCS1_v1_5.new(RSA.importKey(public_key))
    encrypted = base64.b64encode(cipher.encrypt(random_str.encode())).decode()
    ret = {"requestData": request_data, "encrypted": encrypted}
    return ret


def decrypt_data(data):
    try:
        # print(data)
        encrypted = data['encrypted']
        request_data = data['requestData']
        encrypted = encrypted.replace('\r\n', '')

        private_key_rsa = RSA.import_key(private_key)
        cipher_rsa = PKCS1_v1_5.new(private_key_rsa)

        aesKey = cipher_rsa.decrypt(base64.b64decode(encrypted), None)
        # printTip(aesKey)
        AE = AES.new(aesKey, AES.MODE_ECB)
        result_str = AE.decrypt(base64.b64decode(request_data)).decode()
        # 清理额外数据
        result_str = re_strip(result_str, r'[^\]\[{}]')
        # print(result_str)
        result = None
        try:
            result = json.loads(result_str)
        except Exception as e:
            traceback.print_exc()
            printTip(result_str)
        return result
    except Exception as e:
        printError(f'error: {e}')
        traceback.print_exc()


if __name__ == '__main__':
    main()
