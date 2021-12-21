
import io
import pyAesCrypt
class Security:
    def __init__(self):
        self.bufferSize = 1024
        self.password = 'SockMenta'
    def Encrypt(self,text):
        input_data = io.BytesIO(text.encode())
        output_data = io.BytesIO()
        pyAesCrypt.encryptStream(input_data, output_data ,self.password,self.bufferSize)
        # Data to send
        dataToSend = output_data.getvalue()
        return dataToSend 
    def Decrept(self,text):
        fullData = b''
        input_data = io.BytesIO()
        output_data = io.BytesIO()
        fullData = fullData + text 
        # Convert to bytes, get length and seek to beginning
        input_data = io.BytesIO(fullData)
        ctlen= len(input_data.getvalue())
        input_data.seek(0)
        # Decrypt stream
        pyAesCrypt.decryptStream(input_data, output_data,self.password,self.bufferSize, ctlen)
        decrypted= str(output_data.getvalue().decode())
        return decrypted
    