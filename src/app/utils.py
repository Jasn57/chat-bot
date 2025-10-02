from flask import Flask, requests, jsonify, render_template
from openai import OpenAI
from dotenv import dotenv_values