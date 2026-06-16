from chroma.chroma_client import banking_functions, applications, processes, controls, teams, past_circulars

class VectorService:

    @staticmethod
    def search_banking_functions(text):

        result = banking_functions.query(
            query_texts=[text],
            n_results=5
        )

        return result


    @staticmethod
    def search_applications(text):

        result = applications.query(
            query_texts=[text],
            n_results=5
        )

        return result


    @staticmethod
    def search_processes(text):

        result = processes.query(
            query_texts=[text],
            n_results=5
        )

        return result


    @staticmethod
    def search_controls(text):

        result = controls.query(
            query_texts=[text],
            n_results=5
        )

        return result


    @staticmethod
    def search_teams(text):

        result = teams.query(
            query_texts=[text],
            n_results=5
        )

        return result


    @staticmethod
    def search_past_circulars(text):

        result = past_circulars.query(
            query_texts=[text],
            n_results=5
        )

        return result