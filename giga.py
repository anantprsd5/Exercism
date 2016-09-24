class gigasecond:
    def year(self,time):
        self.time=time
        year=self.time/31536000
        l=self.time%31536000
        month=l/2592000
        l=l%2592000
        week=l/604800
        l=l%604800
        days=l/86400
        l=l%86400
        hours=l/3600
        l=l%3600
        minutes=l/60
        l=l%60



    
