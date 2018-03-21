from django.shortcuts import render
from django.shortcurs import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .model import Stock
from .serializers import StockSerializer



# Create your views here.
