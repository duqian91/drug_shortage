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

        # need to add encoding utf-8-sig or there will be importing errors
        imported_data = dataset.load(new_medication.read().decode(encoding='utf-8-sig'), format='csv', headers='True')
        result = medication_resource.import_data(dataset, dry_run=True, raise_errors=True)  # Test the data import
        # take off raise_errors when the test is done
        # add code here to clean the data so that the format will fit with the model
        # needs to have the first column with header "id" for the file to save

        if result.has_errors():
            print('there are errors in the upload process')
            # add a behavior to show user that there is an error

        elif not result.has_errors():
            medication_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'upload.html')
