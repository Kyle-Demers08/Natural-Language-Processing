import os

teams = ['@afcbournemouth', '@ArsenalFC', '@avfcOfficial', '@BrentfordFC', '@OfficialBHAFC','@CPFC','@ChelseaFC','@everton','@fulhamfc','@LUFC','@lcfc','@lfc', '@ManCity', '@manutd', '@NUFC', '@NFFC', '@SouthamptonFC', '@SpursOfficial', '@WestHam','@Wolves']
for i in teams:
    os.system('python pull_tweets.py ' + '"' + i + '"') #use command line to run pull_tweets for each premier league team
    os.system('python pull_text.py < ' + '"' + i + '.jsonl' + '"' + ' > ' + '"' + 'data//' + i + '.txt' + '"') #use command line to run pull_text for each premier league team