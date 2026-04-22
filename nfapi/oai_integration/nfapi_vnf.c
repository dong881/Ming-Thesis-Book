\t\s*void\s+timespec_add_us(struct\s+timespec\s*\*,\s+long\s+)us(,\s*\{\s*=\s*\}\s*\{\n\s*\t-\s*\-.tv_sec%3D\s*\d+;\s*-\s*\d+;\s*\t\s*=\s*\{\s*\}.replace{\s*=\s*"
<diff content for the line to be inserted>


\t\s*(-\s*\-.tv_sec%3D\s*-\s*\d+;\s*-\s*\d+)\s*\t=\s*.replace{\s*=\s*".replace\}\s*\n\s*\t-\s*\-.tv_nsec%3D\s*-\s*\d
