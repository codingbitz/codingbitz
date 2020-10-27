import base64
import os 
import sys 
from PIL import Image   

# Function to compress the image & encode/decode it. 

def compressImg(file, verbose = False): 

    # open the image 
    formats = ('.jpg', '.jpeg','png')
    if sys.argv[2].lower() in formats:
        sys.argv[2] = sys.argv[2].lower()
    picture = Image.open(sys.argv[1]+'.'+sys.argv[2]) 
    picture.save("comp_"+sys.argv[1]+'.'+sys.argv[2], "JPEG", optimize = True,quality = 10) 
    print("Done") 
    return
  
# Driver code 
if __name__ == "__main__": 
    compressImg(sys.argv[1]+'.'+sys.argv[2], verbose = False)
    image = open("comp_"+sys.argv[1]+'.'+sys.argv[2], 'rb')
    print(f'comp_.jpg')
    image_read = image.read()
    # # Read the image file & encode it using base64
    image_64_encode = base64.encodebytes(image_read)
    # # might help if you are planning to embed binary image to html
    txt_1 = b'<img style="width:835px" src="data:image/png;base64,'
    txt_2 = b'"/>'
    txt_res = open(sys.argv[1]+'.'+sys.argv[3],'wb')
    txt_res.write(txt_1.rstrip()+image_64_encode.rstrip()+txt_2.rstrip())
    #decode the encoded value to recreate the file again - might help during image transportation for SerDe
    image_64_decode = base64.decodebytes(image_64_encode) 
    image_result = open("rec_"+sys.argv[1]+'.'+sys.argv[4], 'wb') # create a writable image and write the decoding result
    image_result.write(image_64_decode)
