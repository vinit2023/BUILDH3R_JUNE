program umut_calc_buildh3r_657682b8.aleo;



function sum:
    input r0 as u32.public;
    input r1 as u32.private;
    add r0 r1 into r2;
    output r2 as u32.private;


function subtract:
    input r0 as u32.public;
    input r1 as u32.private;
    sub r0 r1 into r2;
    output r2 as u32.private;


function multiply:
    input r0 as u32.public;
    input r1 as u32.private;
    mul r0 r1 into r2;
    output r2 as u32.private;


function divide:
    input r0 as u32.public;
    input r1 as u32.private;
    div r0 r1 into r2;
    output r2 as u32.private;
