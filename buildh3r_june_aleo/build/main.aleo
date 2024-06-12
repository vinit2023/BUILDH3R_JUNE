program math.aleo;



function main:
    input r0 as u32.public;
    input r1 as u32.private;
    add r0 r1 into r2;
    output r2 as u32.private;


function subtract:
    input r0 as u32.private;
    input r1 as u32.private;
    sub r0 r1 into r2;
    output r2 as u32.private;
