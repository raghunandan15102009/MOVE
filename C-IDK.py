import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A2M0jU7ix4SP8kH1Ix3w2-eyvOuJoxwQzZhxVMSZDmnqbuD6miY7_F7KSvl2ZJQ_49c8-q4ajM_IlnXxbfIDgccQXMeuCPcxeohDMzxN7LjafVhaxdhM2OUz35Ity4P6LiX0-Tk'
    transferData = TransferData(access_token)

    file_from = input("C:\1. Office\Hack\Module 3\projects\C-98")
    file_to = input("C:\1. Office\Hack\Module 3\projects\C-IDK ") 
    
    transferData.upload_file(file_from, file_to)
    print("Just a sample")


main()
