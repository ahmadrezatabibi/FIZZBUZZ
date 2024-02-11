import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Fizzbuzz
from .serializers import FizzbuzzSerializer

# Get an instance of a logger
logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def fizzbuzz_list(request):
    """
    List all Fizzbuzz items or create a new Fizzbuzz item.
    """
    if request.method == 'GET':
        fizzbuzzes = Fizzbuzz.objects.all()
        serializer = FizzbuzzSerializer(fizzbuzzes, many=True)
        logger.info("Retrieved all Fizzbuzz items.")
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = FizzbuzzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Created a new Fizzbuzz item with id: {serializer.instance.fizzbuzz_id}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.error(f"Failed to create a new Fizzbuzz item: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fizzbuzz_detail(request, id):
    """
    Retrieve a Fizzbuzz item by id.
    """
    try:
        fizzbuzz = Fizzbuzz.objects.get(pk=id)
    except Fizzbuzz.DoesNotExist:
        logger.error(f"Fizzbuzz item with id: {id} not found.")
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FizzbuzzSerializer(fizzbuzz)
        logger.info(f"Retrieved Fizzbuzz item with id: {id}.")
        return Response(serializer.data)
