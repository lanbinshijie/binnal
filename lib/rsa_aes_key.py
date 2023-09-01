# RSA公私钥操作
import rsa, os
# 导入AES模块
from Crypto.Cipher import AES

def gernerateKeys():
    # 生成RSA公钥和私钥
    pubkey, privkey = rsa.newkeys(2048)
    # 保存公钥和私钥
    with open('public.pem', 'w+') as f:
        f.write(pubkey.save_pkcs1().decode())
    with open('private.pem', 'w+') as f:
        f.write(privkey.save_pkcs1().decode())

def checkKeys():
    # 判断是否有公钥和私钥
    try:
        with open('public.pem', 'r') as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        with open('private.pem', 'r') as f:
            privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
    except:
        gernerateKeys()
        with open('public.pem', 'r') as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
        with open('private.pem', 'r') as f:
            privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
    return pubkey, privkey

def encryptAESKey(aesKey):
    # 使用公钥加密明文
    pubkey, privkey = checkKeys()
    encrypted_message = rsa.encrypt(aesKey, pubkey)
    return encrypted_message

def decryptAESKey(encrytedAesKey):
    # 使用私钥解密密文
    pubkey, privkey = checkKeys()
    decrypted_message = rsa.decrypt(encrytedAesKey, privkey)
    return decrypted_message

def aesKey():
    # 生成AES密钥
    aesKey = os.urandom(16)
    return aesKey

def aesEncrypt(aesKey, message):
    # 使用AES密钥加密明文
    aes = AES.new(aesKey, AES.MODE_ECB)
    encrypted_message = aes.encrypt(message)
    return encrypted_message

def aesDecrypt(aesKey, encrypted_message):
    # 使用AES密钥解密密文
    aes = AES.new(aesKey, AES.MODE_ECB)
    decrypted_message = aes.decrypt(encrypted_message)
    return decrypted_message

# 加密流程：
# 1. 获取/生成RSA公钥和私钥
# 2. 生成AES密钥（随机数）
# 3. 使用RSA公钥加密AES密钥
# 4. 使用AES密钥（加密后）加密明文

def getEncryptedAESKey():
    # 一键获取aes加密后的key
    aesKey = aesKey()
    encryptedAesKey = encryptAESKey(aesKey)
    return encryptedAesKey

def refreshKeys():
    # 刷新公钥和私钥
    gernerateKeys()