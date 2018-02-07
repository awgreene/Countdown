# Build from the latest Python image
FROM python:latest

# Add the scripts folder from our project to the image
ADD ./scripts ./scripts

# Run our Python script
CMD [ "python", "./scripts/Countdown.py" ]
