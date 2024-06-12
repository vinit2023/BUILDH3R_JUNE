program math.aleo {
    transition main(public a: u32, b: u32) -> u32 {
        let c: u32 = a + b;
        return c;
    }

    transition subtract(private x: u32, private y: u32) -> u32 {
        let z: u32 = x - y;
        return z;
    }
}