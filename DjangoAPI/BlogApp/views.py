from django.shortcuts import render
#from django.views.decorations.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BlogApp.models import BlogTypes, Blogs
from BlogApp.serializers import BlogSerializers, BlogTypeSerializers
from django.views.decorators.csrf import csrf_exempt

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def blogTypeApi(request, id=0):
    if request.method=='GET':
        blogTypes = BlogTypes.objects.all()
        blogTypes_serializer = BlogTypeSerializers(blogTypes, many=True)
        return JsonResponse(blogTypes_serializer.data, safe=False)
    elif request.method=='POST':
        blogType_data=JSONParser().parse(request)
        blogType_serializer = BlogTypeSerializers(data=blogType_data)
        if blogType_serializer.is_valid():
            blogType_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False) 
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method=='PUT':
        blogType_data = JSONParser().parse(request)
        blogType = BlogTypes.objects.get(BlogTypeId=blogType_data['BlogTypeId'])
        blogType_serializer = BlogTypeSerializers(blogType, data=blogType_data)
        if blogType_serializer.is_valid():
            blogType_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed tp Update", safe=False)
    elif request.method=='DELETE':
        toBeRemovedBlogType = BlogTypes.objects.get(BlogTypeId=id)
        toBeRemovedBlogType.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

# blogs API
@csrf_exempt
def blogApi(request, id=0):
    if request.method=='GET':
        blogs = Blogs.objects.all()
        blogs_serializer = BlogSerializers(blogs, many=True)
        return JsonResponse(blogs_serializer.data, safe=False)
    elif request.method=='POST':
        blog_data=JSONParser().parse(request)
        blogs_serializer = BlogSerializers(data=blog_data)
        if blogs_serializer.is_valid():
            blogs_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False) 
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method=='PUT':
        blog_data = JSONParser().parse(request)
        blog = Blogs.objects.get(BlogId=blog_data['BlogId'])
        blogs_serializer = BlogSerializers(blog, data=blog_data)
        if blogs_serializer.is_valid():
            blogs_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed tp Update", safe=False)
    elif request.method=='DELETE':
        toBeRemovedBlog = Blogs.objects.get(BlogId=id)
        toBeRemovedBlog.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def SaveFle(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)