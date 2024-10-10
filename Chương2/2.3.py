import xml.dom.minidom as md

# Phân tích tệp XML
dom = md.parse('sample.xml')

# Lấy phần tử gốc (<company>)
company = dom.documentElement

# Lấy tên công ty
company_name = company.getElementsByTagName('name')[0].firstChild.data
print(f"Tên công ty: {company_name}")

# Lấy các phần tử nhân viên (staff elements)
staff_elements = company.getElementsByTagName('staff')

# Lặp qua các phần tử nhân viên
for staff in staff_elements:
    # Lấy thuộc tính id của nhân viên
    staff_id = staff.getAttribute('id')
    
    # Lấy tên nhân viên
    staff_name = staff.getElementsByTagName('name')[0].firstChild.data
    
    # Lấy lương của nhân viên
    staff_salary = staff.getElementsByTagName('salary')[0].firstChild.data
    
    # In ra thông tin của nhân viên
    print(f"Mã nhân viên: {staff_id}, Tên: {staff_name}, Lương: {staff_salary}")
