## SOURCE 
https://github.com/schollz/python-ocr

## BUILD
docker build --no-cache=true -t ocr .

## RUN
docker run -it -p 5000:5000 ocr

## USAGE
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"url":"https://raw.githubusercontent.com/schollz/ocr-text-extraction/master/test.jpg"}' \
  http://51.83.15.26:5000/detect

