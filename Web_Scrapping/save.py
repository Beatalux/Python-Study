import csv

#place, title,time,pay,date
def save_to_file(jobs,c):
  file=open(f"{c}.csv",mode="w")
  writer=csv.writer(file)
  writer.writerow(["place","title","time","pay","date"])
  if jobs==None:
    writer.writerow(["No info"])
    return
  for job in jobs:
    writer.writerow(list(job.values()))
  return
