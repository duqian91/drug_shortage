from import_export import resources
from .models import Medication

class MedicationResource(resources.ModelResource):
    class Meta:
        model = Medication

        # exclude = ('id')
        
        import_id_fields = ('gespharx_id',)
        # will only import these fields
        # fields = ('gespharx_id', 'din', 'generic_name')

    # # use_transactions = True

    # function used to add empty id header, now used to debug only
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
    #     dataset.insert_col(0, col=["",]*dataset.height, header="id")
        print(dataset)
        
    def before_import_row(self, row, **kwargs):
        print(row)
        # added zeros to the din
        def make_din_eight_digit(num_str):
            if len(num_str) < 8:
                return num_str.zfill(8)
            else:
                return num_str

        
        # apply function to din in row to clean data
        if "din" in row:
            new_din = make_din_eight_digit(row["din"])
            print(new_din)
            row["din"] = new_din
        