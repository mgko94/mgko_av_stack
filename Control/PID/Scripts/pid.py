


# export 
# from mgko_av_stack.Control.PID.Scripts.pid import pidControl
class pidControl :
    def __init__(self,control_time):
        self.p_gain=0
        self.i_gain=0
        self.d_gain=0  
        self.prev_error=0
        self.i_control=0
        self.control_time=control_time
        

    def set_gain(self,p,i,d):
        self.p_gain=p
        self.i_gain=i
        self.d_gain=d


    def pid(self,target_value,current_value):
        error= target_value-current_value
        
        p_control=self.p_gain*error
        self.i_control+=self.i_gain*error*self.control_time
        d_control=self.d_gain*(error-self.prev_error)/self.control_time

        output=p_control+self.i_control+d_control
        self.prev_error=error
        return output






if __name__ == '__main__':
    test = pidControl(0.33)
    test.set_gain(1,0,0)
    print(test.pid(10,0))
