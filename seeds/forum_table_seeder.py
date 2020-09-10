from orator.seeds import Seeder


class ForumTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('foro').insert([
            {
                'nombre': 'aviso de calculo diferencial e integral',
                'numeroUrl': 89531,
                'activo': True,
                'idMateria': 1
            },
            {
                'nombre': 'aviso de estructuras de datos',
                'numeroUrl': 13023,
                'activo': True,
                'idMateria': 2
            },
            {
                'nombre': 'novedades de inglés técnico 1',
                'numeroUrl': 22060,
                'activo': True,
                'idMateria': 3
            },
            {
                'nombre': 'novedades de teoría de la computación 1',
                'numeroUrl': 88332,
                'activo': True,
                'idMateria': 4
            },
            {
                'nombre': 'novedades de programación orientada a objetos',
                'numeroUrl': 197066,
                'activo': True,
                'idMateria': 5
            },
            {
                'nombre': 'avisos ingeniería de requerimientos',
                'numeroUrl': 99114,
                'activo': True,
                'idMateria': 6
            },
            {
                'nombre': 'avisos métodos computacionales para el cálculo',
                'numeroUrl': 101358,
                'activo': True,
                'idMateria': 7
            },
            {
                'nombre': 'novedades teoría de la computación 2',
                'numeroUrl': 100599,
                'activo': True,
                'idMateria': 8
            },
            {
                'nombre': 'cosas nuevas rquitecturas y organización de computadoras 1',
                'numeroUrl': 101850,
                'activo': True,
                'idMateria': 9
            },
            {
                'nombre': 'aviso programación concurrente',
                'numeroUrl': 361446,
                'activo': True,
                'idMateria': 10
            }
        ])

