
import io
import pyAesCrypt
class Security:
    def __init__(self):
        self.bufferSize = 1024
        self.password = 'SockMenta'
    def Encrypt(self,text):
        fIn = io.BytesIO(text.encode())
        fCiph = io.BytesIO()
        pyAesCrypt.encryptStream(fIn, fCiph,self.password,self.bufferSize)
        # Data to send
        dataToSend = fCiph.getvalue()
        return dataToSend 
    def Decrept(self,text):
        fullData = b''
        fCiph = io.BytesIO()
        fDec = io.BytesIO()
        fullData = fullData + text 
        # Convert to bytes, get length and seek to beginning
        fCiph = io.BytesIO(fullData)
        ctlen= len(fCiph.getvalue())
        fCiph.seek(0)
        # Decrypt stream
        pyAesCrypt.decryptStream(fCiph, fDec,self.password,self.bufferSize, ctlen)
        decrypted= str(fDec.getvalue().decode())
        return decrypted
    