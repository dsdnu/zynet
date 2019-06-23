module ReLU  #(parameter dataWidth=16,weightIntWidth=4) (
    input           clk,
    input   [2*dataWidth-1:0]   x,
    output  reg [dataWidth-1:0]  out
);


always @(posedge clk)
begin
    if($signed(x) >= 0)
		if(|x[2*dataWidth-1-:weightIntWidth])
			out <= {1'b0,{(dataWidth-1){1'b1}}}; //positive saturate
		else
			out <= x[2*dataWidth-weightIntWidth-1-:dataWidth];
    else 
        out <= 0;      
end

endmodule