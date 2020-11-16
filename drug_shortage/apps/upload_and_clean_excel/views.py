from django.http import HttpResponse
from django.shortcuts import render

from drug_shortage.apps.upload_and_clean_excel.resources import MedicationResource

from tablib import Dataset

# Create your views here.
def upload(request):
    if request.method == 'POST':
        medication_resource = MedicationResource()
        dataset = Dataset()
        new_medication = request.FILES['myfile']

        imported_data = dataset.load(new_medication.read().decode(), format='csv', headers='True')
        result = medication_resource.import_data(dataset, dry_run=True)  # Test the data import
        # add code here to clean the data so that the format will fit with the model
        # needs to have the first column with header "id" for the file to save

        if result.has_errors():
            print('there are errors in the upload process')

        elif not result.has_errors():
            medication_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'upload.html')
