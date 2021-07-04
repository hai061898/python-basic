def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print ("Chia một số cho 0!")
except Exception as problem:
    print ('Bắt được một exception')
finally:
    print ('Phép tính bị hủy')

# finally là một cách khác để viết lệnh try trong Python. Finally còn được gọi là mệnh đề clean-up/termination vì nó luôn luôn chạy bất kể có lỗi nào xảy ra trong block try. Thường thì các câu lệnh trong finally được dùng để thực hiện công việc giải phóng tài nguyên.