# views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import json

from .models import ProjectMaster, ActivityMaster, DailyProgress
from .forms import ProjectMasterForm, ActivityMasterForm, DailyProgressForm


# API: Return JSON list
@csrf_exempt
def get_all_projects(request):
    if request.method == "GET":
        projects = ProjectMaster.objects.all().values()
        return JsonResponse({"status": "success", "projects": list(projects)}, status=200)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

# HTML: List page (populated by JS calling the API)
def project_list_page(request):
    return render(request, 'project_list.html')

# HTML + API: Create page & POST handler
@csrf_exempt
def create_project(request):
    if request.method == "POST":
        if request.content_type == "application/json":
            data = json.loads(request.body)
        else:
            data = request.POST

        form = ProjectMasterForm(data)
        if form.is_valid():
            project = form.save()
            if request.content_type == "application/json":
                return JsonResponse({
                    "status": "success",
                    "message": "Project created successfully!",
                    "id": project.id
                }, status=200)
            else:
                return redirect('project_list')
        else:
            if request.content_type == "application/json":
                return JsonResponse({
                    "status": "error",
                    "message": "Validation error",
                    "errors": form.errors
                }, status=400)
            else:
                return render(request, 'create_project.html', {'form': form})
    else:
        form = ProjectMasterForm()
        return render(request, 'create_project.html', {'form': form})

# API: Get by ID
@csrf_exempt
def get_project_by_id(request, pk):
    if request.method == "GET":
        try:
            project = ProjectMaster.objects.get(pk=pk)
            return JsonResponse({"status": "success", "project": model_to_dict(project)}, status=200)
        except ProjectMaster.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Project not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

# API: Update by ID
@csrf_exempt
def update_project_by_id(request, pk):
    try:
        project = ProjectMaster.objects.get(pk=pk)
    except ProjectMaster.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Project not found"}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(project, field, value)
        try:
            project.full_clean()
            project.save()
            return JsonResponse({
                "status": "success",
                "message": "Project updated successfully",
                "project": model_to_dict(project)
            }, status=200)
        except ValidationError as e:
            return JsonResponse({"status": "error", "message": "Validation error", "errors": e.message_dict}, status=400)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

# API: Delete by ID
@csrf_exempt
def delete_project_by_id(request, pk):
    try:
        project = ProjectMaster.objects.get(pk=pk)
    except ProjectMaster.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Project not found"}, status=404)

    if request.method == "DELETE":
        project.delete()
        return JsonResponse({"status": "success", "message": "Project deleted successfully"}, status=200)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

def index_page(request):
    return render(request, 'index.html')






# === API: Return all activities ===
@csrf_exempt
def get_all_activities(request):
    if request.method == "GET":
        activities = ActivityMaster.objects.all().values()
        return JsonResponse({"status": "success", "activities": list(activities)}, status=200)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)



# === HTML + API: Create activity ===
@csrf_exempt
def create_activity(request):
    if request.method == "POST":
        if request.content_type == "application/json":
            data = json.loads(request.body)
        else:
            data = request.POST

        form = ActivityMasterForm(data)
        if form.is_valid():
            activity = form.save()
            if request.content_type == "application/json":
                return JsonResponse({
                    "status": "success",
                    "message": "Activity created successfully!",
                    "id": activity.id
                }, status=200)
            else:
                return redirect('activity_list')
        else:
            if request.content_type == "application/json":
                return JsonResponse({
                    "status": "error",
                    "message": "Validation error",
                    "errors": form.errors
                }, status=400)
            else:
                return render(request, 'create_activity.html', {'form': form})
    else:
        form = ActivityMasterForm()
        return render(request, 'create_activity.html', {'form': form})

# === API: Get by ID ===
@csrf_exempt
def get_activity_by_id(request, pk):
    if request.method == "GET":
        try:
            activity = ActivityMaster.objects.get(pk=pk)
            return JsonResponse({"status": "success", "activity": model_to_dict(activity)}, status=200)
        except ActivityMaster.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Activity not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

# === API: Update by ID ===
@csrf_exempt
def update_activity_by_id(request, pk):
    try:
        activity = ActivityMaster.objects.get(pk=pk)
    except ActivityMaster.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Activity not found"}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(activity, field, value)
        try:
            activity.full_clean()
            activity.save()
            return JsonResponse({
                "status": "success",
                "message": "Activity updated successfully",
                "activity": model_to_dict(activity)
            }, status=200)
        except ValidationError as e:
            return JsonResponse({"status": "error", "message": "Validation error", "errors": e.message_dict}, status=400)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)



# === API: Delete by ID ===
@csrf_exempt
def delete_activity_by_id(request, pk):
    try:
        activity = ActivityMaster.objects.get(pk=pk)
    except ActivityMaster.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Activity not found"}, status=404)

    if request.method == "DELETE":
        activity.delete()
        return JsonResponse({"status": "success", "message": "Activity deleted successfully"}, status=200)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)



# === HTML: Activity list page (JS will call API to fill table) ===
def activity_list_page(request):
    return render(request, 'activity_list.html')



# === API: Return all daily progress records ===
@csrf_exempt
def get_all_progress(request):
    if request.method == "GET":
        progresses = DailyProgress.objects.all().values()
        return JsonResponse({"status": "success", "progress": list(progresses)}, status=200)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

# === HTML: Daily progress list page ===
def progress_list_page(request):
    return render(request, 'progress_list.html')

# === HTML + API: Create new daily progress ===
@csrf_exempt
def create_progress(request):
    if request.method == "POST":
        if request.content_type == "application/json":
            data = json.loads(request.body)
        else:
            data = request.POST

        form = DailyProgressForm(data)
        if form.is_valid():
            progress = form.save()
            if request.content_type == "application/json":
                return JsonResponse({
                    "status": "success",
                    "message": "Daily progress created successfully!",
                    "id": progress.id
                }, status=200)
            else:
                return redirect('progress_list')  # Make sure this name matches in urls.py
        else:
            if request.content_type == "application/json":
                return JsonResponse({
                    "status": "error",
                    "message": "Validation error",
                    "errors": form.errors
                }, status=400)
            else:
                return render(request, 'create_progress.html', {'form': form})
    else:
        form = DailyProgressForm()
        return render(request, 'create_progress.html', {'form': form})

# === API: Get progress by ID ===
@csrf_exempt
def get_progress_by_id(request, pk):
    if request.method == "GET":
        try:
            progress = DailyProgress.objects.get(pk=pk)
            return JsonResponse({"status": "success", "progress": model_to_dict(progress)}, status=200)
        except DailyProgress.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Daily progress not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

# === API: Update progress by ID ===
@csrf_exempt
def update_progress_by_id(request, pk):
    try:
        progress = DailyProgress.objects.get(pk=pk)
    except DailyProgress.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Daily progress not found"}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        for field, value in data.items():
            setattr(progress, field, value)
        try:
            progress.full_clean()
            progress.save()
            return JsonResponse({
                "status": "success",
                "message": "Daily progress updated successfully",
                "progress": model_to_dict(progress)
            }, status=200)
        except ValidationError as e:
            return JsonResponse({
                "status": "error",
                "message": "Validation error",
                "errors": e.message_dict
            }, status=400)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)

# === API: Delete progress by ID ===
@csrf_exempt
def delete_progress_by_id(request, pk):
    try:
        progress = DailyProgress.objects.get(pk=pk)
    except DailyProgress.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Daily progress not found"}, status=404)

    if request.method == "DELETE":
        progress.delete()
        return JsonResponse({
            "status": "success",
            "message": "Daily progress deleted successfully"
        }, status=200)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)




# === OPTIONAL: Index page ===
def index_page(request):
    return render(request, 'index.html')
