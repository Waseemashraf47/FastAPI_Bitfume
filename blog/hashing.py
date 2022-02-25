#FOR PASSWORD ENCRYPTION
from passlib.context import CryptContext

pwd_cxt= CryptContext (schemes=["bcrypt"], deprecated="auto")
class Hash ():

    def bcrypt (plain_password:str):
        return pwd_cxt.hash(plain_password)
        
    def verify(plain_password, hashed_password):
        return pwd_cxt.verify(plain_password,hashed_password)