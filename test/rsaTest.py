import rsa

# 生成RSA公钥和私钥
pubkey, privkey = rsa.newkeys(2048)

# 要加密的明文
message = b'Hello, RSA!'

print("公钥:", pubkey)
print("私钥:", privkey)

# 保存公钥和私钥
with open('public.pem', 'w+') as f:
    f.write(pubkey.save_pkcs1().decode())
with open('private.pem', 'w+') as f:
    f.write(privkey.save_pkcs1().decode())

# 使用公钥加密明文
encrypted_message = rsa.encrypt(message, pubkey)

# 使用私钥解密密文
decrypted_message = rsa.decrypt(encrypted_message, privkey)

print("明文:", message)
print("加密后的密文:", encrypted_message)
print("解密后的明文:", decrypted_message)
