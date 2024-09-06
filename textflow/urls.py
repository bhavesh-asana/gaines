from django.urls import path

from . import views

urlpatterns = [
    path("pymupdf/", views.scanner_pymupdf, name="scan_pymupdf"),
    path("folderscan/", views.scan_folder, name="scan_folder")
]
