class rna_transcription(object):
    def rna(self,dna):
        self.list={'G':'C','C':'G','T':'A','A':'U'}
        self.str=""
        for i in dna:
            self.str=self.str+self.list[i]
        print self.str
        
