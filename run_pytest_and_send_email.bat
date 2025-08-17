#!/bin/bash
# Run pytest and generate the HTML report
pytest -m "smoke or regression"
# Run the Python script to send the email
python send_email.py