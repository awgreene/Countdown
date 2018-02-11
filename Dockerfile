# Build from the latest Python 3 Image
FROM python:3

# Add the scripts folder from our project to the image
ADD ./scripts ./scripts

# Run our Python script
CMD python ./scripts/Countdown.py $TIME
