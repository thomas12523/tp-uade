import json

salones = {
                '1': {
                    "activo": True,
                    "nombreSalon": "Chiquimundo",
                    "ubicacion": "San Martín",
                    "capacidad": 30,
                    "telefonos": {
                        "telefono1": "1145678901",
                        "telefono2": "1145678902",
                        "telefono3": "1145678903"
                    }
                },
                '2': {
                    "activo": False,
                    "nombreSalon": "El Peperón",
                    "ubicacion": "Pepe León",
                    "capacidad": 45,
                    "telefonos": {
                        "telefono1": "1167890123",
                        "telefono2": "1167890124",
                        "telefono3": "1167890125"
                    }
                },
                '3': {
                    "activo": True,
                    "nombreSalon": "La Cúpula",
                    "ubicacion": "Belgrano",
                    "capacidad": 60,
                    "telefonos": {
                        "telefono1": "1178901234",
                        "telefono2": "1178901235",
                        "telefono3": "1178901236"
                    }
                },
                '4': {
                    "activo": True,
                    "nombreSalon": "Versalles Hall",
                    "ubicacion": "Versalles",
                    "capacidad": 80,
                    "telefonos": {
                        "telefono1": "1189012345",
                        "telefono2": "1189012346",
                        "telefono3": "1189012347"
                    }
                },
                '5': {
                    "activo": False,
                    "nombreSalon": "Sala Luna",
                    "ubicacion": "Palermo",
                    "capacidad": 50,
                    "telefonos": {
                        "telefono1": "1190123456",
                        "telefono2": "1190123457",
                        "telefono3": "1190123458"
                    }
                },
                '6': {
                    "activo": True,
                    "nombreSalon": "El Rincón",
                    "ubicacion": "Recoleta",
                    "capacidad": 40,
                    "telefonos": {
                        "telefono1": "1123456789",
                        "telefono2": "1123456790",
                        "telefono3": "1123456791"
                    }
                },
                '7': {
                    "activo": True,
                    "nombreSalon": "Sala Oasis",
                    "ubicacion": "Caballito",
                    "capacidad": 35,
                    "telefonos": {
                        "telefono1": "1134567890",
                        "telefono2": "1134567891",
                        "telefono3": "1134567892"
                    }
                },
                '8': {
                    "activo": False,
                    "nombreSalon": "La Estación",
                    "ubicacion": "San Telmo",
                    "capacidad": 70,
                    "telefonos": {
                        "telefono1": "1156789012",
                        "telefono2": "1156789013",
                        "telefono3": "1156789014"
                    }
                },
                '9': {
                    "activo": True,
                    "nombreSalon": "El Paraiso",
                    "ubicacion": "Villa Crespo",
                    "capacidad": 55,
                    "telefonos": {
                        "telefono1": "1167890234",
                        "telefono2": "1167890235",
                        "telefono3": "1167890236"
                    }
                },
                '10': {
                    "activo": True,
                    "nombreSalon": "Sala Tango",
                    "ubicacion": "San Nicolás",
                    "capacidad": 65,
                    "telefonos": {
                        "telefono1": "1178902345",
                        "telefono2": "1178902346",
                        "telefono3": "1178902347"
                    }
                }
            }


f = open("salones.json", "w", encoding="utf-8")
json.dump(salones, f, ensure_ascii=False, indent=4)
f.close()