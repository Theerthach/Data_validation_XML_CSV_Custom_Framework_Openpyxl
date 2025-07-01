# XML vs CSV Data Comparison Framework

This Python project reads an XML file from an AWS S3 bucket and compares its contents with a locally stored CSV file. The results are output into an Excel file, clearly marking matches and mismatches after applying transformations to the XML data to match the CSV format.

---

## 🔧 Features

- ✅ Reads XML file from S3 using `boto3`
- ✅ Reads local CSV file using `pandas`
- ✅ Applies transformations on XML fields (e.g., date format, phone formatting, uppercasing, rounding)
- ✅ Compares transformed XML fields with CSV fields
- ✅ Generates an Excel report with:
  - Original XML and CSV values
  - Transformed XML values
  - Match/Mismatch status
 
## Sample Output
![image](https://github.com/user-attachments/assets/7c8a411e-954e-4953-ad00-75f5a1398ef2)

