# optimal scheduling weighted requests

# creat a job class to control the jobs better
class Job:
    def __init__(self , start , finish , profit):
        self.start = start
        self.finish = finish
        self.profit = profit

# we creat a search fuction to find the job before our
# current job that it's finish time is less than current job
def serach_job(job , start_index):
    
    # set low and high values to find the job
    low = 0 
    high = start_index - 1  

    # creat a loop to find the correct job in job array
    while low <= high: 
        mid = (low + high) // 2
        if job[mid].finish <= job[start_index].start: 
            if job[mid + 1].finish <= job[start_index].start: 
                low = mid + 1
            else: 
                return mid 
        else: 
            high = mid - 1
    return -1


def schedule(job): 
	
    # sorting the jobs array by their finish time
	job = sorted(job, key = lambda j: j.finish) 

	jobs_count = len(job)
    
    
	ans_arr = [0 for _ in range(jobs_count)] 
	ans_arr[0] = job[0].profit; 

    # calculate the answers and set them in
    # ans_arr to 
	for i in range(1, jobs_count): 

        # find the profit of current job
		Prof = job[i].profit
		l = serach_job(job, i)
		if (l != -1): 
			Prof += ans_arr[l]; 

        # find maximum of jobs that can fit in our time
		ans_arr[i] = max(Prof, ans_arr[i - 1]) 

	return ans_arr[jobs_count-1] 


# set the jobs
job = [Job(1, 5, 25), Job(3, 10, 20), Job(6, 19, 110), Job(2, 20, 150)] 


# printing the job's to show the user
def print_job(job):
    c = 0
    for j in job:
        c += 1
        print("job{}:".format(c))
        print("start time:" , j.start)
        print("finish time:" , j.finish)
        print("profit :" , j.profit , end="\n\n")

print_job(job)


#=============un comment the code below for optional job inserting=============
# c = 0
# job = []
# while True:
#     c += 1
#     temp_s = input("please enter job#{} start time:".format(c))
#     temp_f = input("please enter job#{} start time:".format(c))
#     temp_p = input("please enter job#{} start time:".format(c))
#     if temp_s != "" or temp_f != "" or temp_p != "":
#         job.append(Job(temp_s , temp_f , temp_p))
#         print_job(job)
#     else:
#         break



# printing the finall answer
print("Optimal profit is : " , end =""), 
print (schedule(job))

input()

# code written by Yasin Boloorchi. 