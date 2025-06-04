import pandas as pd
from exams.models import Student  # Replace 'exams' with your app name if different

def import_students_from_excel(file_path):
    try:
        df = pd.read_excel(file_path)

        # Normalize column names: strip spaces, lowercase, replace spaces with underscores
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

        # Check for required columns
        required_columns = {'roll_number', 'name', 'class_name', 'year', 'semester'}
        if not required_columns.issubset(set(df.columns)):
            print(f"❌ Missing required columns. Found columns: {df.columns.tolist()}")
            return

        added = 0
        skipped = 0

        for _, row in df.iterrows():
            obj, created = Student.objects.get_or_create(
                roll_number=row['roll_number'],
                defaults={
                    'name': row['name'],
                    'class_name': row['class_name'],
                    'year': str(row['year']),
                    'semester': str(row['semester']),
                }
            )
            if created:
                added += 1
            else:
                skipped += 1

        print(f"✅ Done! {added} students added, {skipped} already existed.")

    except Exception as e:
        print(f"❌ Error importing students: {e}")
